import asyncio
from playwright.async_api import async_playwright
from interface_login import criar_janela

async def preencher_dados_estudante(pagina, ra, digito, senha):
    # 1. Seleciona "Estudante"
    await pagina.get_by_text('Estudante', exact=True).click()

    # 2. Espera o input de RA aparecer
    await pagina.locator("#input-usuario-sed").wait_for(timeout=10000)

    # 3. Preenche RA
    await pagina.fill("#input-usuario-sed", ra)

    # 4. Preenche Dígito (se houver outro campo específico, usar o seletor real)
    # Como você não enviou o HTML do dígito, aqui vamos assumir que ele é o segundo input na tela
    await pagina.locator("input[type='text']").nth(1).fill(digito)

    # 5. Preenche senha
    await pagina.locator("input[type='password']").fill(senha)

    # 6. Clica no botão Acessar
    await pagina.get_by_role('button', name='Acessar').click()

    # 7. Espera o login concluir
    await pagina.wait_for_load_state("networkidle")

    # 8. Vai para Redação
    await pagina.get_by_role("link", name="Redação Paulista").click()
    print("[SUCESSO] Entrou na Redação!")

async def main():
    # Pega dados da interface
    dados = criar_janela()
    ra = dados["ra"]
    digito = dados["digito"]
    senha = dados["senha"]

    async with async_playwright() as pw:
        navegador = await pw.chromium.launch(headless=False)
        pagina = await navegador.new_page()
        await pagina.goto("https://saladofuturo.educacao.sp.gov.br/escolha-de-perfil")

        await preencher_dados_estudante(pagina, ra, digito, senha)

        # Mantém aberto 10s
        await asyncio.sleep(10)
        await navegador.close()

if __name__ == "__main__":
    asyncio.run(main())
