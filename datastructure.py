import streamlit as st
import ast
import codecs
import os

# layout
st.title("Python DataStructure Playground")

c1,c2 = st.columns(2)
c3,c4 = st.columns(2)

with c1:
    inputtext = st.text_input("Provide INPUT Datastructure <without quotes on both side")
with c2:
    opt_input =  st.text_input("Provide Attribute Argument if required","")

choice = st.sidebar.radio('SELECT DATASTRUCTURE',["dictionary","list","set","string","tuple",])

def docfunc_op():
    return open("docout.txt",'r').read()

def func_op():
    replace_none()
    return open("out.txt",'r').read()

def replace_none():
    with open("out.txt") as r:
        text = r.read().replace("None\n", "")
    with open("out.txt", "w") as w:
        w.write(text)

def call_func(inputtext,method_name,opt_input,c):
    doc_f = codecs.open("docout.py", "w", encoding="utf-8")
    f = codecs.open("out.py", "w", encoding="utf-8")
    doc_content = codecs.open("docout.txt", "w", encoding="utf-8")
    content = codecs.open("out.txt", "w", encoding="utf-8")
    if type(inputtext) == str:
        doc_f.write("print(" + chr(34) + inputtext + chr(34) + "." + method_name + ".__doc__" + ")")
        doc_f.flush()
        cmd='python docout.py'
        docp = os.popen(cmd).read()
        doc_content.write(docp)
        doc_content.flush()
        doc_content.close()
        docfunc_op()

        # f.write("print(" + chr(34) + inputtext + chr(34) + "." + method_name + "()" + ")")
        if len(opt_input) > 0:
            f.write("l=" + chr(34) + str(inputtext) + chr(34) + "\n")
            f.write("print(" + chr(34) + inputtext + chr(34) + "." + method_name + "(" + opt_input + "))\n")
            # f.write("print(l)")
        else:
            f.write("print(" + chr(34) + inputtext + chr(34) + "." + method_name + "()" + ")")
        f.flush()
        cmd='python out.py'
        p = os.popen(cmd).read()
        content.write(p)
        content.flush()
        content.close()
        func_op()
    elif type(inputtext) == list:
        doc_f.write("print(" + str(inputtext) + "." + method_name + ".__doc__" + ")")
        doc_f.flush()
        cmd='python docout.py'
        docp = os.popen(cmd).read()
        doc_content.write(docp)
        doc_content.flush()
        doc_content.close()
        docfunc_op()

        if len(opt_input) > 0:
            f.write("l=" + str(inputtext) + "\n")
            f.write("print (l." + method_name + "(" + opt_input + "))\n")
            f.write("print(l)")
        else:
            f.write("print(" + str(inputtext) + "." + method_name + "())")
        f.flush()
        cmd='python out.py'
        p = os.popen(cmd).read()
        content.write(p)
        content.flush()
        content.close()
        func_op()
    elif type(inputtext) == tuple:
        doc_f.write("print(" + str(inputtext) + "." + method_name + ".__doc__" + ")")
        doc_f.flush()
        cmd='python docout.py'
        docp = os.popen(cmd).read()
        doc_content.write(docp)
        doc_content.flush()
        doc_content.close()
        docfunc_op()

        if len(opt_input) > 0:
            f.write("l=" + str(inputtext) + "\n")
            f.write("print (l." + method_name + "(" + opt_input + "))\n")
            f.write("print(l)")
        else:
            f.write("print(" + str(inputtext) + "." + method_name + "())")
        f.flush()
        cmd='python out.py'
        p = os.popen(cmd).read()
        content.write(p)
        content.flush()
        content.close()
        func_op()
    elif type(inputtext) == dict:
        doc_f.write("print(" + str(inputtext) + "." + method_name + ".__doc__" + ")")
        doc_f.flush()
        cmd='python docout.py'
        docp = os.popen(cmd).read()
        doc_content.write(docp)
        doc_content.flush()
        doc_content.close()        
        docfunc_op()

        if len(opt_input) > 0:
            f.write("l=" + str(inputtext) + "\n")
            f.write("print (l." + method_name + "(" + opt_input + "))\n")
            f.write("print(l)")
        else:
            f.write("print(" + str(inputtext) + "." + method_name + "())")
        f.flush()
        cmd='python out.py'
        p = os.popen(cmd).read()
        content.write(p)
        content.flush()
        content.close()
        func_op()
    elif type(inputtext) == set:
        doc_f.write("print(" + str(inputtext) + "." + method_name + ".__doc__" + ")")
        doc_f.flush()
        cmd='python docout.py'
        docp = os.popen(cmd).read()
        doc_content.write(docp)
        doc_content.close()
        doc_content.flush()
        docfunc_op()

        if len(opt_input) > 0:
            f.write("l=" + str(inputtext) + "\n")
            f.write("print (l." + method_name + "(" + opt_input + "))\n")
            f.write("print(l)")
        else:
            f.write("print(" + str(inputtext) + "." + method_name + "())")
        f.flush()
        cmd='python out.py'
        p = os.popen(cmd).read()
        content.write(p)
        content.flush()
        content.close()
        func_op()

# Input/Output Layout section

if len(inputtext) > 0 and choice == "string":
    methods_list = [ele for ele in reversed(dir(inputtext))]
    method_name = st.sidebar.radio('Select Attribute Name',methods_list)
    with c3:
        call_func(inputtext,method_name,opt_input,choice)
        if "None" in str(func_op()):
            func_op = str(func_op())
            func_op.replace("None","")
            st.text_area("Attribute OUTPUT", func_op(), height=50)
        else:
            st.text_area("Attribute OUTPUT", func_op(), height=50)
    with c4:
        st.text_area("Attribute Documentation", docfunc_op(), height=400)
elif len(inputtext) > 0 and choice == "list":
    inputtext = ast.literal_eval(inputtext)
    methods_list = [ele for ele in reversed(dir(inputtext))]
    method_name = st.sidebar.radio('Select Attribute Name', methods_list)
    with c3:
        call_func(inputtext,method_name,opt_input,choice)
        st.text_area("Attribute OUTPUT", func_op(), height=50)
    with c4:
        st.text_area("Attribute Documentation", docfunc_op(), height=400)
elif len(inputtext) > 0 and choice == "tuple":
    inputtext = ast.literal_eval(inputtext)
    methods_list = [ele for ele in reversed(dir(inputtext))]
    method_name = st.sidebar.radio('Select Attribute Name', methods_list)
    with c3:
        call_func(inputtext,method_name,opt_input,choice)
        st.text_area("Attribute OUTPUT", func_op(), height=50)
    with c4:
        st.text_area("Attribute Documentation", docfunc_op(), height=400)
elif len(inputtext) > 0 and choice == "dictionary":
    inputtext = ast.literal_eval(inputtext)
    methods_list = [ele for ele in reversed(dir(inputtext))]
    method_name = st.sidebar.radio('Select Attribute Name', methods_list)
    with c3:
        call_func(inputtext,method_name,opt_input,choice)
        st.text_area("Attribute OUTPUT", func_op(), height=50)
    with c4:
        st.text_area("Attribute Documentation", docfunc_op(), height=400)
elif len(inputtext) > 0 and choice == "set":
    inputtext = ast.literal_eval(inputtext)
    methods_list = [ele for ele in reversed(dir(inputtext))]
    method_name = st.sidebar.radio('Select Attribute Name', methods_list)
    with c3:
        call_func(inputtext,method_name,opt_input,choice)
        st.text_area("Attribute OUTPUT", func_op(), height=50)
    with c4:
        st.text_area("Attribute Documentation", docfunc_op(), height=400)
