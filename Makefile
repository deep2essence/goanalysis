run: clean
	@if [ -d "output" ]; then mkdir output;fi
	@python3 goanalyze.py
clean:
	@rm -rf results/*.own.lst
	@rm -rf results/common.lst
