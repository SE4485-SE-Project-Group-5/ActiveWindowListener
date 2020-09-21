echo 'Building React App...'
cd react-ui
yarn build
if [ $? -ne 0 ]; then
  echo "npm build in react-ui failed"
  exit 1
fi
cd ..

echo 'Cleaning up old builds...'
rm -rf build
rm -rf dist
rm -rf templates
rm -rf static
mkdir templates
cp -r react-ui/build/index.html templates/index.html
cp -r react-ui/build/static static/
mkdir -p static/icons
cp default.png static/icons

echo 'Building exe...'
poetry run pyinstaller -w --add-data "templates;templates"  --add-data "static;static" --add-data "mongo;mongo" -y flair.py
if [ $? -ne 0 ]; then
  echo "build failed"
  exit 1
fi

echo "Flair.exe created. Navigate to dist/ and double click flair.exe or run ./flair.exe in git-bash to launch the application. May take a couple seconds to launch"
rm -rf *.spec
