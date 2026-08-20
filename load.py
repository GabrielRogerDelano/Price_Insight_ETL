from db import Session

def load(df, model, mapping):
    with Session() as session:
        objects = []
    
        for _, row in df.iterrows():
            dados = {
                atributo: row[coluna]
                for atributo, coluna in mapping.items()
            }

            objects.append(model(**dados))
        session.add_all(objects)
        session.commit()
    