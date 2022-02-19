run: clean
	@if [ -d "results" ]; then mkdir results;fi
	@python3 goanalyze.py
clean:
	@rm -rf results/*.own.lst
	@rm -rf results/common.lst
