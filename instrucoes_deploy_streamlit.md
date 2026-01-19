# Instruções para Deploy do Streamlit no Community Cloud

## Passo a Passo

### 1. Acesse o Streamlit Community Cloud
Vá para: **https://share.streamlit.io/**

### 2. Faça Login com GitHub
Clique em "Sign in with GitHub" e autorize o acesso.

### 3. Crie um Novo App
Clique em **"New app"** no canto superior direito.

### 4. Configure o App
Preencha os campos:

| Campo | Valor |
|-------|-------|
| **Repository** | `LeandroCrespo/bolao-copa-2026` |
| **Branch** | `main` |
| **Main file path** | `datathon_passos_magicos/streamlit/app.py` |

### 5. Deploy
Clique em **"Deploy!"** e aguarde alguns minutos.

### 6. Pronto!
Você receberá uma URL pública no formato:
`https://[seu-app].streamlit.app`

---

## Estrutura de Arquivos no Repositório

```
datathon_passos_magicos/
├── streamlit/
│   ├── app.py                              # Aplicação principal
│   ├── requirements.txt                    # Dependências
│   ├── modelo_risco_defasagem.pkl          # Modelo treinado
│   ├── scaler.pkl                          # Normalizador
│   ├── features.txt                        # Lista de features
│   ├── threshold.txt                       # Threshold otimizado
│   └── BASE_DE_DADOS_PEDE_2024_DATATHON.xlsx  # Dados
```

---

## Possíveis Problemas e Soluções

### Erro de Dependências
Se houver erro de instalação, verifique se o `requirements.txt` está correto:
```
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.23.0
scikit-learn>=1.2.0
plotly>=5.15.0
openpyxl>=3.1.0
```

### Erro de Caminho de Arquivo
Os caminhos no `app.py` devem ser relativos à pasta `streamlit/`:
```python
# Correto
model = pickle.load(open('modelo_risco_defasagem.pkl', 'rb'))

# Se não funcionar, use:
import os
script_dir = os.path.dirname(__file__)
model_path = os.path.join(script_dir, 'modelo_risco_defasagem.pkl')
```

---

## Link do Repositório
**https://github.com/LeandroCrespo/bolao-copa-2026**
