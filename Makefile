run:
	./run.sh
run9b:
	./run9b.sh

k:
	./kill.sh

w:
	curl -X GET "http://127.0.0.1:9000/api/ai/WriteBlogRandomlyWithLLM?model=Gemma2_LLM" -H  "Request-Origion:SwaggerBootstrapUi" -H  "accept:*/*"

i:
	pip3 install -r requirements.txt

ca:
	conda activate gemma-2-27b-it