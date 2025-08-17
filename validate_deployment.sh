#!/bin/bash

# Production Deployment Validation Script
# This script validates that the Euystacio system is ready for production deployment

echo "🚀 Euystacio Production Deployment Validator"
echo "=============================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Counters
TOTAL_CHECKS=0
PASSED_CHECKS=0

check_file() {
    local file="$1"
    local description="$2"
    TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
    
    if [ -f "$file" ]; then
        echo -e "  ${GREEN}✅${NC} $description"
        PASSED_CHECKS=$((PASSED_CHECKS + 1))
        return 0
    else
        echo -e "  ${RED}❌${NC} $description - File not found: $file"
        return 1
    fi
}

check_content() {
    local file="$1"
    local pattern="$2"
    local description="$3"
    TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
    
    if [ -f "$file" ] && grep -q "$pattern" "$file"; then
        echo -e "  ${GREEN}✅${NC} $description"
        PASSED_CHECKS=$((PASSED_CHECKS + 1))
        return 0
    else
        echo -e "  ${RED}❌${NC} $description - Pattern not found in $file"
        return 1
    fi
}

echo ""
echo "📁 Backend Files Validation"
echo "----------------------------"

# Check backend files
check_file "deployed-backend/app.py" "Backend application exists"
check_file "deployed-backend/euystacio.py" "Euystacio kernel exists"
check_file "deployed-backend/requirements.txt" "Requirements file exists"

# Check backend configuration
check_content "deployed-backend/app.py" "debug=False" "Production debug setting"
check_content "deployed-backend/app.py" "host=\"0.0.0.0\"" "Production host setting"

echo ""
echo "🌐 Frontend Files Validation"
echo "-----------------------------"

# Check frontend files
check_file "deployed-frontend/index.html" "Frontend main page exists"
check_file "deployed-frontend/connect.html" "Frontend connect page exists"
check_file "deployed-frontend/config.js" "Frontend configuration exists"

# Check frontend configuration
check_content "deployed-frontend/config.js" "euystacio-moonrise.onrender.com" "Production backend URL"

echo ""
echo "📚 Documentation Validation"
echo "----------------------------"

# Check documentation
check_file "README.md" "README documentation exists"
check_file "DEPLOYMENT.md" "Deployment documentation exists"
check_file "PRODUCTION_CHECKLIST.md" "Production checklist exists"

# Check documentation content
check_content "README.md" "Production Deployment" "README has production info"
check_content "DEPLOYMENT.md" "euystacio-moonrise.onrender.com" "Deployment docs have correct URL"

echo ""
echo "🔧 Configuration Consistency"
echo "-----------------------------"

# Check URL consistency
BACKEND_URL="euystacio-moonrise.onrender.com"
TOTAL_CHECKS=$((TOTAL_CHECKS + 1))

if grep -q "$BACKEND_URL" "deployed-frontend/config.js" && grep -q "$BACKEND_URL" "config.js"; then
    echo -e "  ${GREEN}✅${NC} Backend URL consistent across configurations"
    PASSED_CHECKS=$((PASSED_CHECKS + 1))
else
    echo -e "  ${RED}❌${NC} Backend URL inconsistent across configurations"
fi

echo ""
echo "🧪 Python Dependencies Test"
echo "----------------------------"

TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
cd deployed-backend
if python3 -c "import flask, flask_cors; print('Dependencies available')" 2>/dev/null; then
    echo -e "  ${GREEN}✅${NC} Python dependencies are available"
    PASSED_CHECKS=$((PASSED_CHECKS + 1))
else
    echo -e "  ${YELLOW}⚠️${NC}  Python dependencies not installed (run: pip install -r requirements.txt)"
fi
cd ..

echo ""
echo "📊 Validation Summary"
echo "====================="
echo "Total Checks: $TOTAL_CHECKS"
echo "Passed: $PASSED_CHECKS"
echo "Failed: $((TOTAL_CHECKS - PASSED_CHECKS))"

if [ $PASSED_CHECKS -eq $TOTAL_CHECKS ]; then
    echo ""
    echo -e "${GREEN}🎉 All checks passed! System is ready for production deployment.${NC}"
    echo ""
    echo "Next steps:"
    echo "1. Deploy backend to Render.com as 'euystacio-moonrise'"
    echo "2. Deploy frontend to GitHub Pages"
    echo "3. Test the deployed system end-to-end"
    echo "4. Use PRODUCTION_CHECKLIST.md for detailed deployment steps"
    exit 0
else
    echo ""
    echo -e "${RED}⚠️  Some checks failed. Please fix the issues before deploying.${NC}"
    exit 1
fi