class IpnsEnsError(Exception):
    pass


class TheGraphQueryError(IpnsEnsError):
    pass


class ENSLookupError(TheGraphQueryError):
    pass