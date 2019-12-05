rm -r prjs
rm -r enc
mkdir complied
java -jar ./bin/compiler.jar --compilation_level ADVANCED_OPTIMIZATIONS --js beta_js/CPL.js
./bin/javascript-obfuscator ./beta_js/ --output ./enc
mkdir prjs
cp ./enc/beta_js/* ./prjs/
sed -i 's/beta_js/prjs/g' *.html
