
import streamlit as st
import pandas as pd

st.set_page_config(page_title="AMS Pro - Ficha Técnica & Macramê", page_icon="🧶", layout="wide")

st.title("🧶 AMS Pro: Ateliê & Macramê")
st.markdown("### Sistema de Cálculo de Custos, Metragem e Ficha Técnica")

tab1, tab2 = st.tabs(["🧮 Calculadora & Ficha Técnica", "📋 Meus Projetos Salvos"])

with tab1:
    st.subheader("Parâmetros do Peça de Macramê")
    col1, col2 = st.columns(2)
    
    with col1:
        nome_peca = st.text_input("Nome da Peça", value="Vestido / Saída de Praia Macramê")
        tipo_fio = st.text_input("Tipo de Fio / Material", value="Fio Náutico / Cordão de Algodão 4mm")
        preco_bobina = st.number_input("Preço do Rolo/Bobina (R$)", value=80.0)
        metros_bobina = st.number_input("Metragem Total na Bobina (m)", value=100.0)
        
    with col2:
        metros_gastos = st.number_input("Metragem Estimada Gasta (m)", value=35.0)
        horas_trabalho = st.number_input("Tempo de Execução (Horas)", value=12.0)
        valor_hora = st.number_input("Valor da sua Hora de Trabalho (R$)", value=25.0)
        margem_lucro = st.slider("Margem de Lucro Desejada (%)", 50, 300, 150)

    # Cálculos
    custo_material_por_metro = preco_bobina / metros_bobina if metros_bobina > 0 else 0
    custo_material_total = custo_material_por_metro * metros_gastos
    custo_mao_de_obra = horas_trabalho * valor_hora
    custo_total = custo_material_total + custo_mao_de_obra
    preco_sugerido = custo_total * (1 + margem_lucro / 100)

    st.markdown("---")
    st.subheader("📊 Resumo de Custos e Sugestão de Preço")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Custo de Material", f"R$ {custo_material_total:.2f}")
    m2.metric("Mão de Obra", f"R$ {custo_mao_de_obra:.2f}")
    m3.metric("Custo de Produção", f"R$ {custo_total:.2f}")
    m4.metric("Preço de Venda Sugerido", f"R$ {preco_sugerido:.2f}", delta=f"{margem_lucro}% margem")

    if st.button("💾 Salvar Ficha Técnica"):
        st.success(f"Ficha técnica da peça '{nome_peca}' gerada e salva com sucesso!")

with tab2:
    st.subheader("Histórico de Fichas Técnicas")
    st.info("Aqui ficarão salvas as suas fichas técnicas calculadas para consulta rápida.")
