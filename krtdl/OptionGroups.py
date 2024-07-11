

def create_option_groups() -> List[OptionGroup]:
    option_group_list: List[OptionGroup] = []
    for name, options in krtdl_option_groups.items():
        option_group_list.append(OptionGroup(name=name, options=options))

    return option_group_list
