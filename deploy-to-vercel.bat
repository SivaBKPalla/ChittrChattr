@echo off
echo ========================================
echo    ChittrChattr Deployment Helper
echo ========================================
echo.

echo This script will help you deploy ChittrChattr to the web!
echo.

echo Choose your deployment method:
echo.
echo 1. Deploy to Vercel (Recommended - No Node.js needed)
echo 2. Deploy to Netlify (Easy - No Node.js needed)
echo 3. Install Node.js and run locally
echo 4. Show deployment instructions
echo.

set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" goto vercel
if "%choice%"=="2" goto netlify
if "%choice%"=="3" goto local
if "%choice%"=="4" goto instructions
goto invalid

:vercel
echo.
echo ========================================
echo    Deploying to Vercel
echo ========================================
echo.
echo 1. Go to https://vercel.com
echo 2. Sign up with GitHub
echo 3. Click "New Project"
echo 4. Import your repository
echo 5. Click "Deploy"
echo.
echo Your site will be live in minutes!
echo.
pause
goto end

:netlify
echo.
echo ========================================
echo    Deploying to Netlify
echo ========================================
echo.
echo 1. Go to https://netlify.com
echo 2. Sign up for free
echo 3. Drag and drop this entire folder
echo 4. Your site is live!
echo.
pause
goto end

:local
echo.
echo ========================================
echo    Installing Node.js
echo ========================================
echo.
echo 1. Go to https://nodejs.org
echo 2. Download the LTS version
echo 3. Install it
echo 4. Restart this command prompt
echo 5. Run: npm install
echo 6. Run: npm start
echo.
echo Your site will run on http://localhost:3000
echo.
pause
goto end

:instructions
echo.
echo ========================================
echo    Deployment Instructions
echo ========================================
echo.
echo Open DEPLOYMENT.md for detailed instructions
echo.
start DEPLOYMENT.md
pause
goto end

:invalid
echo.
echo Invalid choice. Please run the script again.
echo.
pause
goto end

:end
echo.
echo Thank you for using ChittrChattr!
echo.
