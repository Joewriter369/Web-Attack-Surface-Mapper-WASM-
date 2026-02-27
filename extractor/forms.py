def extract_forms(soup):
    forms = []

    for form in soup.find_all("form"):
        action = form.get("action")
        method = form.get("method", "get").lower()

        inputs = []
        for inp in form.find_all("input"):
            if inp.get("name"):
                inputs.append(inp.get("name"))

        forms.append({
            "action": action,
            "method": method,
            "inputs": inputs
        })

    return forms

