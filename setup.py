#!/usr/bin/env python3
"""
Euystacio Setup Script
Automatically extracts ZIP files and sets up the deployment environment.
"""

import os
import zipfile
import shutil
import argparse


def extract_zip(zip_path, extract_to, overwrite=False):
    """Extract a ZIP file to the specified directory."""
    if not os.path.exists(zip_path):
        print(f"❌ ZIP file not found: {zip_path}")
        return False
    
    if os.path.exists(extract_to) and not overwrite:
        print(f"⚠️  Directory already exists: {extract_to}")
        print("   Use --overwrite to replace existing files")
        return False
    
    if overwrite and os.path.exists(extract_to):
        print(f"🗑️  Removing existing directory: {extract_to}")
        shutil.rmtree(extract_to)
    
    os.makedirs(extract_to, exist_ok=True)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    
    print(f"✅ Extracted {zip_path} to {extract_to}")
    return True


def setup_backend(overwrite=False):
    """Extract and setup the backend."""
    print("🔧 Setting up backend...")
    
    backend_zip = "euystacio-backend.zip"
    backend_dir = "deployed-backend"
    
    if extract_zip(backend_zip, backend_dir, overwrite):
        # Copy enhanced files to override the ones from ZIP
        enhanced_files = ["app.py", "euystacio.py", "requirements.txt"]
        for enhanced_file in enhanced_files:
            if os.path.exists(enhanced_file):
                shutil.copy2(enhanced_file, backend_dir)
                print(f"📋 Updated {enhanced_file} with enhanced version")
        
        # Copy any additional config files if needed
        config_files = ["render.yaml"]
        for config_file in config_files:
            if os.path.exists(config_file):
                shutil.copy2(config_file, backend_dir)
                print(f"📋 Copied {config_file} to backend directory")
        
        print("🚀 Backend setup complete!")
        print(f"   Deploy the '{backend_dir}' directory to your hosting service")
        return True
    
    return False


def setup_frontend(overwrite=False):
    """Extract and setup the frontend."""
    print("🎨 Setting up frontend...")
    
    frontend_zip = "euystacio-site.zip"
    frontend_dir = "deployed-frontend"
    
    if extract_zip(frontend_zip, frontend_dir, overwrite):
        # Copy enhanced files to override the ones from ZIP
        enhanced_files = ["config.js"]
        for enhanced_file in enhanced_files:
            if os.path.exists(enhanced_file):
                shutil.copy2(enhanced_file, frontend_dir)
                print(f"📋 Added {enhanced_file} to frontend")
        
        # Copy enhanced connect.html if it exists
        if os.path.exists("connect-enhanced.html"):
            shutil.copy2("connect-enhanced.html", os.path.join(frontend_dir, "connect.html"))
            print(f"📋 Updated connect.html with enhanced version")
        print("🌐 Frontend setup complete!")
        print(f"   Upload the files from '{frontend_dir}' to your web hosting service")
        print("   Remember to update the BACKEND_URL in connect.html")
        return True
    
    return False


def setup_full_package(overwrite=False):
    """Extract and setup the full package from euystacio-full-package directory."""
    print("📦 Setting up full package...")
    
    full_package_dir = "euystacio-full-package"
    if not os.path.exists(full_package_dir):
        print(f"❌ Full package directory not found: {full_package_dir}")
        return False
    
    # Extract backend from full package
    backend_zip = os.path.join(full_package_dir, "backend", "euystacio-backend.zip")
    backend_dir = "deployed-backend"
    
    if os.path.exists(backend_zip):
        extract_zip(backend_zip, backend_dir, overwrite)
    
    # Extract frontend from full package
    frontend_zip = os.path.join(full_package_dir, "frontend", "euystacio-site.zip")
    frontend_dir = "deployed-frontend"
    
    if os.path.exists(frontend_zip):
        extract_zip(frontend_zip, frontend_dir, overwrite)
    
    print("📚 Full package setup complete!")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Setup script for Euystacio deployment"
    )
    parser.add_argument(
        "--component", 
        choices=["backend", "frontend", "full", "all"],
        default="all",
        help="Which component to set up (default: all)"
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing directories"
    )
    
    args = parser.parse_args()
    
    print("🌑 Euystacio Setup Script")
    print("=" * 30)
    
    success = True
    
    if args.component in ["backend", "all"]:
        success &= setup_backend(args.overwrite)
    
    if args.component in ["frontend", "all"]:
        success &= setup_frontend(args.overwrite)
    
    if args.component == "full":
        success &= setup_full_package(args.overwrite)
    
    if success:
        print("\n🎉 Setup completed successfully!")
        print("\nNext steps:")
        print("1. Deploy backend directory to your hosting service (e.g., Render)")
        print("2. Upload frontend files to your web hosting (e.g., GitHub Pages)")
        print("3. Update BACKEND_URL in connect.html with your backend URL")
    else:
        print("\n❌ Setup encountered errors. Please check the output above.")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())