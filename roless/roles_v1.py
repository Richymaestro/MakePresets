from roless.base import Method

class ScopeRevokeFunction(Method):
    """Disallows a specific function signature on a scoped target."""
    name = "scopeRevokeFunction"
    in_signature = [("role", "uint16"), ("target_address", "address"), ("function_sig", "bytes4")]

    def __init__(self, role: int, target_address: str, function_sig: str):
        self.role = role
        self.target_address = target_address
        self.function_sig = function_sig

class ScopeAllowFunction(Method):
    """Allows a specific function signature on a scoped target."""
    name = "scopeAllowFunction"
    in_signature = [("role", "uint16"), ("target_address", "address"), ("function_sig", "bytes4"), ("options", "uint8")]

    def __init__(self, role: int, target_address: str, function_sig: str, options: int):
        self.role = role
        self.target_address = target_address
        self.function_sig = function_sig   
        self.options = options 

class ScopeFunction(Method):
    """Sets scoping rules for a function, on a scoped address."""
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

class ScopeTarget(Method):
    """Scopes calls to an address, limited to specific function signatures, and per function scoping rules."""
    name = "scopeTarget"
    in_signature = [("role", "uint16"), ("target_address", "address")]

    def __init__(self, role: int, target_address: str):
        self.role = role
        self.target_address = target_address

class AllowTarget(Method):
    """Allows all calls made to an address."""
    name = "allowTarget"
    in_signature = [("role", "uint16"), ("target_address", "address"), ("options", "uint8")]

    def __init__(self, role: int, target_address: str, options: int):
        self.role = role
        self.target_address = target_address
        self.options = options

