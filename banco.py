import argparse


class ContaBancaria:
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gerir Uma Conta Bancária")
    parser.add_argument(
        "-A",
        "--acao",
        required=True,
        choices=["depositar", "levantar", "saldo", "info"],
        help="Ação a Executar",
    )
    parser.add_argument(
        "-V", "--valor", type=float, help="Valor para Depositar ou Levantar"
    )
    args = parser.parse_args()

    conta = ContaBancaria("Carlos", 500.0, 100.0)

    if args.acao == "depositar":
        if args.valor is None:
            print("É Necessário Fornecer o Valor Para Depositar.")
        else:
            conta.depositar(args.valor)
    elif args.acao == "levantar":
        if args.valor is None:
            print("É Necessário Fornecer o Valor Para Levantar (-v VALOR).")
        else:
            conta.levantar(args.valor)
    elif args.acao == "saldo":
        conta.exibir_saldo()
    elif args.acao == "info":
        conta.exibir_info()
