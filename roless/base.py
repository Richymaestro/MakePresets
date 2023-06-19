import json
from web3 import Web3

AvatarSafeAddress = object()
Address = str


class InvalidArgument(Exception):
    pass


class Method:
    name = None
    in_signature = []
    out_signature = []
    fixed_arguments = dict()
    value: int = 0  # Eg: amount of ETH in mainnet, xDai in GC

    def __init__(self):
        pass

    @property
    def args_list(self):
        return [self._get_arg_value(e) for e in self.in_signature]

    @property
    def data(self):
        contract = Web3().eth.contract(address=None, abi=self.abi)
        result = contract.encodeABI(fn_name=self.name, args=self.args_list)
        return result

    @property
    def short_signature(self):
        types = ",".join([self._get_arg_type(e) for e in self.in_signature])
        return f"{self.name}({types})"

    @property
    def abi(self):
        inputs = [self._abi_for(e) for e in self.in_signature]
        outputs = [self._abi_for(e) for e in self.out_signature]
        abi = {"name": self.name, "type": "function", "inputs": inputs, "outputs": outputs}
        return json.dumps([abi])

    @property
    def contract_address(self):
        return self.target_address


    def call(self, web3, *args, **kwargs):
        contract = web3.eth.contract(address=self.target_address, abi=self.abi)
        return contract.functions[self.name](*self.args_list).call(*args, **kwargs)

    def _get_arg_value(self, element):
        arg_name, arg_type = element
        if type(arg_type) in (list, tuple):
            value = tuple(self._get_arg_value(e) for e in arg_type)
        else:
            if arg_name in self.fixed_arguments:
                value = self.fixed_arguments[arg_name]
                if value is AvatarSafeAddress:
                    value = self.avatar
            else:
                value = getattr(self, arg_name)
        return value

    def _abi_for(self, element):
        name, _type = element
        if type(_type) in (list, tuple):
            value = {"name": name,
                     "type": "tuple",
                     "components": [self._abi_for(e) for e in _type]
                     }
        else:
            value = {"name": name, "type": _type}
        return value

    def _get_arg_type(self, element):
        _type = element[1]
        if type(_type) in (list, tuple):
            types = ",".join([self._get_arg_type(e) for e in _type])
            value = f"({types})"
        else:
            value = _type
        return value

    