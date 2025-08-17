#!/bin/bash

# Euystacio Deployment Script
# Automates the complete deployment process

set -e  # Exit on any error

echo "🌑 Euystacio Deployment Script"
echo "==============================="

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed"
    exit 1
fi

# Check if we're in the right directory
if [[ ! -f "setup.py" ]] || [[ ! -f "euystacio-backend.zip" ]]; then
    echo "❌ Please run this script from the Euystacio repository root"
    exit 1
fi

# Parse command line arguments
OVERWRITE=false
COMPONENT="all"
BACKEND_URL=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --overwrite)
            OVERWRITE=true
            shift
            ;;
        --component)
            COMPONENT="$2"
            shift 2
            ;;
        --backend-url)
            BACKEND_URL="$2"
            shift 2
            ;;
        --help)
            echo "Usage: $0 [OPTIONS]"
            echo "Options:"
            echo "  --overwrite         Overwrite existing deployment directories"
            echo "  --component TYPE    Deploy specific component (backend|frontend|all)"
            echo "  --backend-url URL   Set backend URL in frontend configuration"
            echo "  --help              Show this help message"
            exit 0
            ;;
        *)
            echo "❌ Unknown option: $1"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

# Run setup script
echo "🔧 Running setup script..."
if $OVERWRITE; then
    python3 setup.py --component "$COMPONENT" --overwrite
else
    python3 setup.py --component "$COMPONENT"
fi

# Update backend URL if provided
if [[ -n "$BACKEND_URL" ]] && [[ -d "deployed-frontend" ]]; then
    echo "🔗 Updating backend URL in frontend configuration..."
    
    if [[ -f "deployed-frontend/connect.html" ]]; then
        # Create a backup
        cp "deployed-frontend/connect.html" "deployed-frontend/connect.html.backup"
        
        # Update the BACKEND_URL in connect.html
        sed -i.tmp "s|const BACKEND_URL = \"[^\"]*\"|const BACKEND_URL = \"$BACKEND_URL\"|g" "deployed-frontend/connect.html"
        rm -f "deployed-frontend/connect.html.tmp"
        
        echo "✅ Updated BACKEND_URL to: $BACKEND_URL"
    else
        echo "⚠️  connect.html not found in deployed-frontend directory"
    fi
fi

# Create deployment instructions
echo "📝 Creating deployment instructions..."
cat > DEPLOYMENT.md << EOF
# Deployment Instructions

Generated on: $(date)

## Backend Deployment (deployed-backend/)

### Option 1: Render
1. Create a new Web Service on Render
2. Upload all files from \`deployed-backend/\` directory
3. Set start command: \`python app.py\`
4. Deploy and note the URL

### Option 2: Railway/Heroku
1. Create new app
2. Upload files from \`deployed-backend/\`
3. Ensure \`requirements.txt\` is present
4. Deploy with Python buildpack

## Frontend Deployment (deployed-frontend/)

### Option 1: GitHub Pages
1. Create a new repository or use existing one
2. Upload files from \`deployed-frontend/\` to repository
3. Enable GitHub Pages in repository settings
4. Set source to main branch, root folder

### Option 2: Netlify/Vercel
1. Create new site
2. Upload files from \`deployed-frontend/\`
3. Deploy static site

## Configuration

Backend URL in frontend: ${BACKEND_URL:-"https://euystacio-moonrise.onrender.com/"}

## Testing
1. Visit your frontend URL
2. Login with:
   - Username: hannesmitterer
   - Password: moon-rise
3. Test sending pulses and viewing the chart

## API Endpoints
- POST /pulse - Send new pulse data
- GET /log - Retrieve all pulse data
- GET /status - Get system status
EOF

echo ""
echo "🎉 Deployment preparation complete!"
echo ""
echo "📁 Files created:"
if [[ -d "deployed-backend" ]]; then
    echo "   • deployed-backend/ - Ready for backend hosting"
fi
if [[ -d "deployed-frontend" ]]; then
    echo "   • deployed-frontend/ - Ready for frontend hosting"
fi
echo "   • DEPLOYMENT.md - Detailed deployment instructions"
echo ""
echo "🚀 Next steps:"
echo "   1. Read DEPLOYMENT.md for detailed instructions"
echo "   2. Deploy backend to your hosting service"
echo "   3. Deploy frontend to your web hosting"
echo "   4. Update frontend with your backend URL if not already done"