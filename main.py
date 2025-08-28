import asyncio
from playwright.async_api import async_playwright

async def preencher_dados_estudante(pagina):
    clicar_sou_estudante = pagina.get_by_text('Estudante', exact= 'true')
    await clicar_sou_estudante.click()

    ra = pagina.get_by_role('textbox',  name = 'Ex.:' )
    await ra.fill('')

    digito_ra = pagina.get_by_role('textbox', name= '0' )
    await digito_ra.fill('')

    senha = pagina.get_by_role('textbox', name= 'Digite sua senha')
    await senha.fill('')

#TODO criar função pra clicar no botão "acessar"

async def main():
    async with async_playwright() as pw:
        navegador = await pw.chromium.launch(headless=False)
        pagina = await navegador.new_page()
        await pagina.goto('https://saladofuturo.educacao.sp.gov.br/escolha-de-perfil')
        await preencher_dados_estudante(pagina)
        await pagina.wait_for_timeout(100000)

if __name__ == '__main__':
    asyncio.run(main())
