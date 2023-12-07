import pandas as pd
from chalicelib.dddpy.generator.usecase.generator_usecase import GeneratorUsecase
from chalicelib.dddpy.generator.usecase.generator_cmd_schema import CreateGeneatorSchema



def read_excel_and_create_generator(file_path):
    # Lee el archivo Excel
    df = pd.read_excel(file_path)

    # Inicializa el GeneratorUsecase
    generator_usecase = GeneratorUsecase()

    # Itera sobre cada fila del DataFrame
    for index, row in df.iterrows():
        # Crea un objeto CreateGeneatorSchema con los datos de la fila
        state_value = '' if pd.isna(row['state']) else row['state']

        create_generator_schema = CreateGeneatorSchema(
            title=row['name'],
            language=row['language'],
            insurance=row['name'],  # Asumiendo que el tipo de seguro es el nombre, ajusta según sea necesario
            device=row['device'],
            media=row['media'],
            state=state_value,
            type=row['type'],
            brand_id=row['brand_id'],
            brand=row['brand'],
            urls=[row['url']]  # Asume que hay una sola URL por fila, ajusta según sea necesario
        )

        # Llama al método create de GeneratorUsecase
        response = generator_usecase.create(create_generator_schema)
        print(response)

if __name__ == "__main__":
    # Ruta al archivo Excel
    file_path = "import.xlsx"
    read_excel_and_create_generator(file_path)
