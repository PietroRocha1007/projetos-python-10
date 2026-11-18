import json

tarefas = []

def salvar_tarefas():
    with open("tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)


def mostrar_menu():
    print("\n" + "=" * 50)
    print("             GERENCIADOR DE TAREFAS")
    print("=" * 50)
    print("  [1] Adicionar tarefa")
    print("  [2] Mostrar tarefas")
    print("  [3] Buscar tarefa")
    print("  [4] Concluir tarefa")
    print("  [5] Excluir tarefa")
    print("  [6] Sair")
    print("-" * 50)

def carregar_tarefas():
    global tarefas

    try:
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            tarefas = json.load(arquivo)

    except FileNotFoundError:
        tarefas = []


def adicionar_tarefa():
    tarefas_nome = input(">> Nome da tarefa: ").strip()
    tarefas_status = input(">> Status (Pendente/Concluída): ").strip().lower()
    if tarefas_status == "pendente":
        tarefas_status = "Pendente"
    elif tarefas_status == "concluída":
        tarefas_status = "Concluída"
    else:
        print("! Status inválido. A tarefa será adicionada como 'Pendente'.")
        tarefas_status = "Pendente"

    tarefa = {"nome": tarefas_nome, "status": tarefas_status}
    tarefas.append(tarefa)
    salvar_tarefas()
    print("-" * 50)
    print(f"+ Tarefa '{tarefas_nome}' adicionada com sucesso!")


def mostrar_tarefas():
    print("\n--- TAREFAS CADASTRADAS " + "-" * 26)
    if not tarefas:
        print("  (Nenhuma tarefa cadastrada.)")
        print("-" * 50)
        return

    for i, tarefa in enumerate(tarefas, start=1):
        print(f"  {i:02} | Nome: {tarefa['nome']} | Status: {tarefa['status']}")
    print("-" * 50)


def buscar_tarefa():
    if not tarefas:
        print("! Nenhuma tarefa cadastrada. Adicione uma tarefa primeiro.")
        return

    tarefa_buscada = input(">> Nome da tarefa que deseja buscar: ").strip()
    for tarefa in tarefas:
        if tarefa["nome"] == tarefa_buscada:
            print("-" * 50)
            print("  TAREFA ENCONTRADA")
            print(f"  Nome   : {tarefa['nome']}")
            print(f"  Status : {tarefa['status']}")
            print("-" * 50)
            return
    print("! Tarefa não encontrada.")


def concluir_tarefa():
    if not tarefas:
        print("! Nenhuma tarefa cadastrada. Adicione uma tarefa primeiro.")
        return

    tarefa_concluida = input(">> Nome da tarefa que deseja concluir: ").strip()
    for tarefa in tarefas:
        if tarefa["nome"] == tarefa_concluida:
            tarefa["status"] = "Concluída"
            salvar_tarefas()
            print(f"+ Tarefa '{tarefa['nome']}' marcada como concluída.")
            return
    print("! Tarefa não encontrada.")


def excluir_tarefa():
    if not tarefas:
        print("! Nenhuma tarefa cadastrada. Adicione uma tarefa primeiro.")
        return

    tarefa_excluida = input(">> Nome da tarefa que deseja excluir: ").strip()
    for tarefa in tarefas:
        if tarefa["nome"] == tarefa_excluida:
            tarefas.remove(tarefa)
            salvar_tarefas()
            print(f"+ Tarefa '{tarefa['nome']}' excluída com sucesso.")
            return
    print("! Tarefa não encontrada.")


carregar_tarefas()
while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        mostrar_tarefas()
    elif opcao == "3":
        buscar_tarefa()
    elif opcao == "4":
        concluir_tarefa()
    elif opcao == "5":
        excluir_tarefa()
    elif opcao == "6":
        print("\n" + "=" * 50)
        print("  Encerrando o programa. Até logo!")
        print("=" * 50)
        break
    else:
        print("! Opção inválida. Escolha uma opção de 1 a 6.")


# Aprendendo Git na prática