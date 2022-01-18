echo
echo "Installing Python 3.9..."
install-pkg python3.9

echo
echo "Installing Python dependencies..."
poetry install

echo
echo "Installing JavaScript dependencies..."
npm install

echo
echo "Patching Transcrypt Parcel Plugin..."
patch -uN ./node_modules/parcel-plugin-transcrypt/asset.js <<-END
--- asset0.js	1985-10-26 01:15:00.000000000 -0700
+++ asset.js	2022-01-17 22:34:36.648376535 -0800
@@ -1,5 +1,5 @@
 const Asset = require('parcel-bundler/src/Asset');
-const logger = require('parcel-bundler/src/Logger');
+const logger = require('@parcel/logger/src/Logger');
 const child_process = require('child_process');
 const path = require('path');
 const fs = require('fs');
@@ -11,7 +11,7 @@
 // package.json, then modify as needed.
 const DEFAULT_PACKAGE_CONFIG = {
     "parcel-plugin-python": {
-        "command": "python3 -m transcrypt",
+        "command": "python3.9 -m transcrypt",
         "arguments": [
             /*  note that --build should normally not be used because multiple .py entry points         */
             /*  cause transcrypt to delete the first run's __target__ as it starts the second call.     */
END
echo "Transcrypt Parcel Plugin patch completed!"
echo

