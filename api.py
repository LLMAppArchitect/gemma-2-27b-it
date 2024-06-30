import time
from datetime import datetime

import torch
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

seg = "==================================================================================================================================================================================================="
app = FastAPI()
model_name = "google/gemma-2-27b-it"

pipe = pipeline(
    "text-generation",
    model=model_name,
    model_kwargs={
        "torch_dtype": torch.bfloat16,
        "quantization_config": {
            "load_in_8bit": True
        }
    },
    device_map="auto"
)


# 定义输入数据的模型
class InputData(BaseModel):
    prompt: str
    max_tokens: int


@app.post("/v1/chat/completions")
def completions(input_data: InputData):
    print(seg)
    s = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    start = time.time()
    print(f'开始时间:{s}')

    print(input_data.prompt)

    messages = [
        {"role": "user", "content": input_data.prompt},
    ]
    outputs = pipe(
        messages,
        max_new_tokens=input_data.max_tokens,
        do_sample=False,
    )
    assistant_response = outputs[0]["generated_text"][-1]["content"]

    print(assistant_response)

    print(seg)
    t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    end = time.time()
    print(f'结束时间:{t}')
    print(f'耗时：{end - start} 秒)')

    return assistant_response


if __name__ == '__main__':
    # 启动API服务
    uvicorn.run(app,
                host="0.0.0.0",
                port=8227,
                log_level="info",
                access_log=False,
                timeout_keep_alive=5)
