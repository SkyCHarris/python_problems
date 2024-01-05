data = row[index-1].value   # -1 grabs correct column for some reason, teehee
        data_column.append(data)
        date_pattern = re.search(r'\d{4}-\d{1,2}-\d{1,2}')
        for i in data_column:
            if date_pattern in i:
        
        cleaned_data = [x for x in data_column if date_pattern not in data]
    return data_column