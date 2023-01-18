import streamlit as st

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

st.title("素数判定アプリ")
n = st.number_input("数字を入力してください", value=0)
if is_prime(n):
    st.success(f"{n}は素数です")
else:
    st.error(f"{n}は素数ではありません")