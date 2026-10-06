import streamlit as st

st.set_page_config(page_title="ÁXIUS | Demo Mobile", page_icon="🦅", layout="centered")

st.markdown("""
<style>
.stApp{background:#050d18}
.block-container{max-width:680px;padding:1rem 1rem 4rem}
[data-testid="stSidebar"]{display:none}
.brand{display:flex;align-items:center;gap:10px;margin-bottom:12px}
.eagle{font-size:32px}.brand-name{color:#fff;font-size:24px;font-weight:900;letter-spacing:3px}
.brand-sub{color:#7f9ab5;font-size:9px;letter-spacing:1.7px}
.demo{background:#142d46;border:1px solid #2c587d;color:#8fc7f5;border-radius:30px;padding:6px 10px;font-size:9px;font-weight:800}
.hero{background:linear-gradient(145deg,#0c2036,#0a1626);border:1px solid #234564;border-radius:22px;padding:23px 20px;margin:10px 0 14px}
.kicker{color:#79b6e7;font-size:10px;font-weight:800;letter-spacing:1.7px;text-transform:uppercase}
.hero h1{color:#fff;font-size:29px;line-height:1.08;margin:9px 0}
.hero p{color:#a8bed2;font-size:13px;line-height:1.55}
.online{display:inline-block;color:#8fe0bd;background:#0e2b28;border:1px solid #285b50;border-radius:30px;padding:7px 11px;font-size:9px;font-weight:800}
.row{display:flex;gap:9px;margin-bottom:15px}.kpi{flex:1;background:#0a1726;border:1px solid #1d3850;border-radius:16px;padding:13px 11px}
.label{color:#7791a8;font-size:9px;text-transform:uppercase;letter-spacing:.8px}.value{color:#fff;font-size:24px;font-weight:850;margin-top:5px}
.section{color:#fff;font-size:16px;font-weight:800;margin:21px 0 9px}
.card,.pub,.alert{background:#0a1726;border:1px solid #1d3850;border-radius:16px;padding:14px;margin-bottom:9px}
.title{color:#fff;font-size:13px;font-weight:750}.meta,.text{color:#8ca4b8;font-size:10px;line-height:1.5;margin-top:5px}
.status{display:inline-block;margin-top:9px;border-radius:20px;padding:5px 8px;font-size:8px;font-weight:800}
.green{background:#0c2925;border:1px solid #24564d;color:#83d9b7}.yellow{background:#2c2511;border:1px solid #685421;color:#e5c96b}
.red{border-left:4px solid #d55c69}.yel{border-left:4px solid #d2b24e}.ok{border-left:4px solid #55b996}
.tag{color:#83bce7;font-size:9px;font-weight:800}.date{color:#71889e;font-size:9px}
.process{color:#fff;font-size:12px;font-weight:750;margin-top:7px}
.footer{color:#5f7488;text-align:center;font-size:9px;line-height:1.5;margin-top:28px;padding-top:16px;border-top:1px solid #172d42}
div.stButton>button{border-radius:12px;min-height:44px;font-weight:750}
</style>
""", unsafe_allow_html=True)

if "demo" not in st.session_state: st.session_state.demo = False

if not st.session_state.demo:
    st.markdown("""<div style="text-align:center;padding:34px 10px 20px">
    <div style="font-size:64px">🦅</div><div style="color:#fff;font-size:35px;font-weight:900;letter-spacing:5px">ÁXIUS</div>
    <div style="color:#7f9ab5;font-size:10px;letter-spacing:2px">INTELIGÊNCIA JURÍDICA</div></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="hero"><div class="kicker">Demonstração gratuita</div>
    <h1>Tecnologia que antecipa.<br>Informação que protege.</h1>
    <p>Uma experiência mobile do ÁXIUS para mostrar como o monitoramento jurídico pode trabalhar continuamente por um escritório.</p>
    <div class="online">● AMBIENTE DE DEMONSTRAÇÃO</div></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="card"><div class="title">O que você verá</div>
    <div class="meta">✓ Visão geral do escritório<br>✓ Monitoramentos ativos<br>✓ Publicações encontradas<br>✓ Central de alertas<br>✓ Inteligência jurídica</div></div>""", unsafe_allow_html=True)
    if st.button("🦅  ENTRAR NA DEMONSTRAÇÃO", use_container_width=True, type="primary"):
        st.session_state.demo=True; st.rerun()
    st.markdown('<div class="footer">ÁXIUS • MAGALHÃES PUBLICAÇÕES<br>Demonstração comercial — dados fictícios</div>', unsafe_allow_html=True)
    st.stop()

monitoramentos=[
("VALE S/A","Parte","TST • TRT3 • TJMG","ATIVO","green"),
("SUZANO S.A.","Parte","TST • TRT2 • TJSP","ATIVO","green"),
("LARA, PONTES & NERY","Advogados","TJSP • TRT2 • TRF3","ATIVO","green"),
("DR. GIOVANNI","Parte + Advogado","TJSP • TJMG","ATENÇÃO","yellow")]
publicacoes=[
("TST","VALE S/A","0001234-56.2026.5.00.0001","Nova comunicação disponibilizada."),
("TJSP","SUZANO S.A.","1009876-44.2026.8.26.0100","Movimentação processual identificada."),
("TRT3","VALE S/A","0012345-77.2026.5.03.0001","Intimação localizada pelo ÁXIUS."),
("TJSP","DR. GIOVANNI","1014567-88.2026.8.26.0100","Publicação prioritária para análise.")]

st.markdown("""<div class="brand"><div class="eagle">🦅</div><div>
<div class="brand-name">ÁXIUS</div><div class="brand-sub">INTELIGÊNCIA JURÍDICA</div></div>
<div class="demo">DEMO</div></div>""", unsafe_allow_html=True)

pagina=st.segmented_control("Navegação",["Início","Monitoramentos","Publicações","Alertas","Inteligência"],default="Início",label_visibility="collapsed")

if pagina=="Início":
    st.markdown("""<div class="hero"><div class="kicker">Central de inteligência</div>
    <h1>Bom dia,<br>Magalhães Publicações.</h1>
    <p>O ÁXIUS está atento aos seus monitoramentos jurídicos e pronto para transformar movimentação em informação.</p>
    <div class="online">● MONITORAMENTO OPERACIONAL</div></div>""",unsafe_allow_html=True)
    st.markdown("""<div class="row"><div class="kpi"><div class="label">Publicações</div><div class="value">899</div></div>
    <div class="kpi"><div class="label">Hoje</div><div class="value">37</div></div><div class="kpi"><div class="label">Alertas</div><div class="value">03</div></div></div>""",unsafe_allow_html=True)
    st.markdown('<div class="section">Publicações recentes</div>',unsafe_allow_html=True)
    for t,p,proc,res in publicacoes[:3]:
        st.markdown(f'<div class="pub"><span class="tag">{t} • {p}</span><span class="date"> Hoje</span><div class="process">{proc}</div><div class="text">{res}</div></div>',unsafe_allow_html=True)
    st.markdown('<div class="section">Central de alertas</div>',unsafe_allow_html=True)
    st.markdown('<div class="alert red"><div class="title">🔴 Atenção necessária</div><div class="text">Nova publicação prioritária identificada em monitoramento.</div></div><div class="alert yel"><div class="title">🟡 Nova movimentação</div><div class="text">O ÁXIUS encontrou uma nova comunicação no DJEN.</div></div>',unsafe_allow_html=True)

elif pagina=="Monitoramentos":
    st.markdown('<div class="section">Monitoramentos ativos</div>',unsafe_allow_html=True)
    for nome,tipo,trib,status,cor in monitoramentos:
        st.markdown(f'<div class="card"><div class="title">{nome}</div><div class="meta">{tipo}<br>{trib}</div><div class="status {cor}">● {status}</div></div>',unsafe_allow_html=True)

elif pagina=="Publicações":
    st.markdown('<div class="section">Publicações encontradas</div>',unsafe_allow_html=True)
    busca=st.text_input("Pesquisar",placeholder="Processo, parte ou tribunal...")
    dados=publicacoes if not busca else [p for p in publicacoes if busca.lower() in " ".join(p).lower()]
    for t,p,proc,res in dados:
        st.markdown(f'<div class="pub"><span class="tag">{t} • {p}</span><span class="date"> 05/10/2026</span><div class="process">{proc}</div><div class="text">{res}</div></div>',unsafe_allow_html=True)

elif pagina=="Alertas":
    st.markdown('<div class="section">Central de alertas</div>',unsafe_allow_html=True)
    st.markdown('<div class="alert red"><div class="title">🔴 Publicação prioritária</div><div class="text">Nova comunicação exige atenção no monitoramento DR. GIOVANNI.</div></div><div class="alert yel"><div class="title">🟡 Nova publicação</div><div class="text">Movimentação identificada no TST vinculada à VALE S/A.</div></div><div class="alert ok"><div class="title">🟢 Sistema operacional</div><div class="text">Todos os monitoramentos demonstrativos estão ativos.</div></div>',unsafe_allow_html=True)

else:
    st.markdown('<div class="section">Inteligência jurídica</div>',unsafe_allow_html=True)
    st.markdown("""<div class="hero"><div class="kicker">Leitura estratégica</div>
    <h1>O ÁXIUS não apenas encontra.<br>Ele organiza.</h1>
    <p>Acompanhe concentração por tribunal, volume de movimentações e prioridades de atenção em uma única visão.</p></div>""",unsafe_allow_html=True)
    st.markdown("""<div class="row"><div class="kpi"><div class="label">Tribunais</div><div class="value">08</div></div>
    <div class="kpi"><div class="label">Processos</div><div class="value">214</div></div><div class="kpi"><div class="label">Prioridades</div><div class="value">07</div></div></div>""",unsafe_allow_html=True)
    st.markdown('<div class="section">Atividade por tribunal</div>',unsafe_allow_html=True)
    for tribunal,volume in [("TST",42),("TJSP",31),("TRT3",18),("TRF3",12)]:
        st.markdown(f'<div class="card"><div style="display:flex;justify-content:space-between;color:#fff;font-size:11px;font-weight:750"><span>{tribunal}</span><span>{volume} movimentações</span></div><div style="margin-top:8px;height:6px;background:#16283a;border-radius:10px"><div style="width:{min(volume*2,100)}%;height:6px;background:#6ba9d6;border-radius:10px"></div></div></div>',unsafe_allow_html=True)

st.markdown('<div class="footer">ÁXIUS • Tecnologia que Antecipa. Informação que Protege.<br>MAGALHÃES PUBLICAÇÕES • DEMONSTRAÇÃO COMERCIAL<br><br><b>Dados apresentados nesta demonstração são fictícios.</b></div>',unsafe_allow_html=True)
