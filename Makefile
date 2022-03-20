all:
	git add .
	git commit -m "generated files on `date +'%Y-%m-%d'`";
	git push --force
