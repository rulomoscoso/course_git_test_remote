import streamlit as st

st.title("Conversor de temperatura")

modo = st.radio("Convertir de:", ["Celsius a Fahrenheit", "Fahrenheit a Celsius"])
valor = st.number_input("Valor")

if modo == "Celsius a Fahrenheit":
    resultado = valor * 9 / 5 + 32
    st.write(f"{valor} C son {round(resultado, 2)} F")
    st.success(f"**{round(resultado, 2)} F**")
    st.caption(f"{valor} C convertidos a Fahrenheit")
else:
    resultado = (valor - 32) * 5 / 9
    st.write(f"{valor} F son {round(resultado, 2)} C")
    st.success(f"**{round(resultado, 2)} C**")
    st.caption(f"{valor} F convertidos a Celsius")