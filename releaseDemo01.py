import streamlit as st

# 设置页面标题
st.set_page_config(page_title="简易计算器", page_icon="🧮")

st.title("🧮 简易计算器")

# 输入框
num1 = st.number_input("数字 1", value=0.0)
num2 = st.number_input("数字 2", value=0.0)
op = st.selectbox("运算符", ["+", "-", "*", "/"])

# 计算逻辑
if st.button("计算"):
    if op == "+":
        res = num1 + num2
    elif op == "-":
        res = num1 - num2
    elif op == "*":
        res = num1 * num2
    else:
        if num2 == 0:
            res = "❌ 错误：不能除以 0"
        else:
            res = num1 / num2
    st.success(f"✅ 结果 = {res}")
