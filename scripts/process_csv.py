import os
from datetime import datetime
import argparse

import pandas as pd

print("Script Python rodando no Docker!")
df = pd.read_csv("/app/order_details.csv")  
print(df.head())

def read_csv(file_path):
    """
    Lê o arquivo CSV e retorna um DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        print("CSV lido com sucesso!")
        return df
    except Exception as e:
        print(f"Erro ao ler o CSV: {e}")
        return None

def save_to_local(df, base_dir, table_name, execution_date):
    """
    Salva o DataFrame em um arquivo local, organizado por data.
    """
    try:
        # Cria o diretório se não existir
        output_dir = os.path.join(base_dir, table_name, execution_date)
        os.makedirs(output_dir, exist_ok=True)

        # Define o caminho do arquivo de saída
        output_file = os.path.join(output_dir, f"{table_name}.csv")

        # Salva o DataFrame em CSV
        df.to_csv(output_file, index=False)
        print(f"Arquivo salvo em: {output_file}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

def main():
    # Configura o parser de argumentos
    parser = argparse.ArgumentParser(description="Processa o arquivo order_details.csv e salva localmente.")
    parser.add_argument("--execution_date", required=True, help="Data de execução no formato YYYY-MM-DD")
    args = parser.parse_args()

    # Define os caminhos
    csv_file_path = "data/order_details.csv"  # Caminho para o arquivo CSV
    base_output_dir = "/data/csv"  # Diretório base para salvar os arquivos

    # Lê o CSV
    df = read_csv(csv_file_path)

    if df is not None:
        # Salva os dados localmente
        save_to_local(df, base_output_dir, "order_details", args.execution_date)

if __name__ == "__main__":
    main()