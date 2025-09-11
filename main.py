import asyncio
from playwright.async_api import async_playwright
from interface_login import criar_janela

async def preencher_dados_estudante(pagina, ra, digito, senha):
    # Seleciona "Estudante"
    await pagina.get_by_text('Estudante', exact=True).click()
    await pagina.locator("#input-usuario-sed").wait_for(timeout=10000)

    # Preenche RA, dígito e senha
    await pagina.fill("#input-usuario-sed", ra)
    await pagina.locator("input[type='text']").nth(1).fill(digito)
    await pagina.locator("input[type='password']").fill(senha)

    # Clica Acessar
    await pagina.get_by_role('button', name='Acessar').click()
    await pagina.wait_for_load_state("networkidle")

    # Clica no primeiro botão Redação Paulista
    await pagina.get_by_role("link", name="Redação Paulista").click()

async def preencher_redacao(pagina, redacao_texto):
    # Hover na div da tarefa para expandir
    div_tarefa = pagina.locator("div.MuiPaper-root.css-16dazv1")
    await div_tarefa.wait_for(state="visible", timeout=10000)
    await div_tarefa.hover()
    await asyncio.sleep(0.5)  # tempo para animação

    # Clique no botão usando data-testid
    botao_prosseguir = pagina.get_by_test_id("botao-tarefa-sp-76597340")
    await botao_prosseguir.wait_for(state="visible", timeout=10000)
    await botao_prosseguir.click(force=True)

    # Espera a textarea da Redação aparecer e preenche
    textarea_redacao = pagina.get_by_role("textbox", name="Redação")
    await textarea_redacao.wait_for(state="visible", timeout=10000)
    await textarea_redacao.click()
    await textarea_redacao.fill(redacao_texto)

    # Botões extras
    botoes_extra = ["Salvar como Rascunho", "Enviar Redação", "Confirmar", "Avançar"]
    for nome_botao in botoes_extra:
        try:
            btn = pagina.get_by_role("button", name=nome_botao)
            await btn.wait_for(state="visible", timeout=5000)
            await btn.click()
        except:
            pass

async def main():
    # Pega dados da interface
    dados = criar_janela()
    ra = dados["ra"]
    digito = dados["digito"]
    senha = dados["senha"]
    redacao_texto = dados["redacao"]

    async with async_playwright() as pw:
        navegador = await pw.chromium.launch(channel="chrome", headless=False)
        pagina = await navegador.new_page()
        await pagina.goto("https://saladofuturo.educacao.sp.gov.br/escolha-de-perfil")

        # Login
        await preencher_dados_estudante(pagina, ra, digito, senha)

        # Redação
        await preencher_redacao(pagina, redacao_texto)

        await asyncio.sleep(10)
        await navegador.close()

if __name__ == "__main__":
    asyncio.run(main())

