rm -r prjs
rm -r enc
./bin/javascript-obfuscator ./beta_js/ --output ./enc
mkdir prjs
cp ./enc/beta_js/* ./prjs/
sed -i 's/beta_js/prjs/g' *.html
