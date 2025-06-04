from relato import cadastrar_relator, cadastrar_relato, buscar_relatos, listar_relatos
import json

def menu():
    while True:
        print("\n--- GeoRelato - Cadastro de Catástrofes Naturais ---")
        print("1. Cadastrar relator")
        print("2. Cadastrar relato")
        print("3. Listar todos os relatos")
        print("4. Buscar relatos por filtro")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_relator()
        elif opcao == '2':
            cadastrar_relato()
        elif opcao == '3':
            listar_relatos()
        elif opcao == '4':
            buscar_relatos()
        elif opcao == '5':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
