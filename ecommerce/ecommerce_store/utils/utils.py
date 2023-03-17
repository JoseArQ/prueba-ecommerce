""" in this module you will find auxiliar functions for complement api implementation"""


def is_valid_body(expected_body : list, body : dict)->bool:
    """method for validate if an body request contains expected body params
    
    Params: 
        - expected_body: List[str]. list with params expected for body requests.
        - body: dict. Input body request.
    
    Returns:
        bool. True if all request body params exist. False in otherwise. 
    """
    for param in expected_body:
        if not param in body.keys():
            return False
    
    return True