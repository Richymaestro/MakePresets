from roless.base import Method

class ScopeRevokeFunction(Method):
    """what does it do :P"""
    name = "scopeRevokeFunction"
    in_signature = [("role", "uint16"), ("target_address", "address"), ("function_sig", "bytes4")]

    def __init__(self, role: int, target_address: str, function_sig: str):
        self.role = role
        self.target_address = target_address
        self.function_sig = function_sig

class ScopeFunction(Method):
    name = "scopeFunction"
    in_signature = [("role","uint16"), ("target_address", "address"),
                    ("function_sig", "address"), ("is_param_scoped", "bool"),
                    ("param_type", "uint8[]"), ("param_comp", "uint8[]"),
                    ("comp_value", "bytes[]"), ("options","uint8")
                    ]

    def __init__(self, role: int, target_address: str, function_sig: str,
                is_param_scoped: bool, param_type: list, param_comp: list,
                comp_value: list, options: int):
        self.role = role
        self.target_address = target_address
        self.function_sig = function_sig 
        self.is_param_scoped = is_param_scoped
        self.param_typed = param_type
        self.param_comp = param_comp
        self.comp_value = comp_value
        self.options = options

class  ScopeTarget(Method):
    name = "scopeTarget"
    in_signature = [("role", "uint16"), ("target_address", "address")]

    def __init__(self, role: int, target_address: str):
        self.role = role
        self.target_address = target_address

class ScopeRevokeFunction(Method):
    """what does it do :P"""
    name = "scopeAllowFunction"
    in_signature = [("role", "uint16"), ("target_address", "address"), 
                    ("function_sig", "bytes4"), ("options", "uint8")]

    def __init__(self, role: int, target_address: str, function_sig: str, options: int):
        self.role = role
        self.target_address = target_address
        self.function_sig = function_sig
        self.options = options


