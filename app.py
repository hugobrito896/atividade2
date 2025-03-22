import streamlit as st

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def kelvin_para_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    st.title("Conversor de Temperatura")

    temperatura = st.number_input("Digite a temperatura:", value=0.0)
    escala_original = st.selectbox("De:", ("Celsius", "Fahrenheit", "Kelvin"))
    escala_destino = st.selectbox("Para:", ("Celsius", "Fahrenheit", "Kelvin"))

    if st.button("Converter"):
        if escala_original == escala_destino:
            resultado = temperatura
        elif escala_original == "Celsius" and escala_destino == "Fahrenheit":
            resultado = celsius_para_fahrenheit(temperatura)
        elif escala_original == "Celsius" and escala_destino == "Kelvin":
            resultado = celsius_para_kelvin(temperatura)
        elif escala_original == "Fahrenheit" and escala_destino == "Celsius":
            resultado = fahrenheit_para_celsius(temperatura)
        elif escala_original == "Fahrenheit" and escala_destino == "Kelvin":
            resultado = fahrenheit_para_kelvin(temperatura)
        elif escala_original == "Kelvin" and escala_destino == "Celsius":
            resultado = kelvin_para_celsius(temperatura)
        elif escala_original == "Kelvin" and escala_destino == "Fahrenheit":
            resultado = kelvin_para_fahrenheit(temperatura)

        st.success(f"Resultado: {resultado:.2f} {escala_destino}")

if __name__ == "__main__":
    main()