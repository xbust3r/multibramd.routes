
@routing_generator.route(f"{PREFIX}/migrate", methods=["GET"])
def migrate():
    try:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        logging.info(f"Current directory: {dir_path}")
        file_path = os.path.join(dir_path, "import.xlsx")
        logging.info(f"Reading file: {file_path}")
        df = pd.read_excel(file_path)
        generator_usecase = GeneratorUsecase()

        for index, row in df.iterrows():
            state_value = "NA" if pd.isna(row["state"]) else row["state"]
            title_value = "" if pd.isna(row["title"]) else row["title"]

            create_generator_schema = CreateGeneatorSchema(
                title=title_value,
                language=row["language"],
                insurance=row["insurance"], 
                device=row["device"],
                media=row["media"],
                state=state_value,
                type=row["type"],
                brand_id=row["brand_id"],
                brand=row["brand"],
                system=row["system"],
                urls=[row["url"]],
            )
            response = generator_usecase.create(create_generator_schema)
            logging.info(f"Successfully created generator for row {index}: {response}")

    except FileNotFoundError as e:
        error_message = f"File not found: {str(e)}"
        logging.error(error_message)
        error_response = ResponseErrorSchema(success=False, message=error_message)
        return Response(body=error_response.dict(), status_code=500)
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        logging.error(error_message)
        error_response = ResponseErrorSchema(success=False, message=error_message)
        return Response(body=error_response.dict(), status_code=500)

    return Response(
        body=ResponseSuccessSchema(
            success=True, message="Migration completed successfully"
        ).dict(),
        status_code=200,
    )
