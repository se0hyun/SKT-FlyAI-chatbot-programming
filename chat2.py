# gradio 사용하기
import gradio as gr

def greet(name):
    return "Hello " + name + "!"    #내가 입력한 값까지 합쳐서 출력

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

demo.launch(share=True)   