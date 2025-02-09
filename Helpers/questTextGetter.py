def questTextGetter(mainBody, questDetails):
    if mainBody:
        # Get quest title and objective
        title = mainBody.find("h1")
        if title:
            objective = title.next_sibling
            if objective and isinstance(objective, str):
                questDetails["objective"] = objective.strip()

        # Get description
        description_header = mainBody.find("h3", text="Description")
        if description_header:
            description = description_header.next_sibling
            if description and isinstance(description, str):
                questDetails["description"] = description.strip()

        # Get completion text
        completion_div = mainBody.find("div", id="completion")
        if completion_div:
            questDetails["completion"] = completion_div.text.strip()

    return questDetails
