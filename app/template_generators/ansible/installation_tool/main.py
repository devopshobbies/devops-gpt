from .nginx import ansible_nginx_install
def ansible_tool_install(input):
    match input.tool:
        case 'nginx':
            return ansible_nginx_install()
        case _:
            raise ValueError('please select a valid tool for installation')