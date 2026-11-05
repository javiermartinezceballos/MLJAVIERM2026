from .hf_loader import HFDatasetLoader

__all__ = ["HFDatasetLoader", "Reportes", "RegresionLineal", "ClasificadorTexto"]


def __getattr__(name: str):
    if name == "Reportes":
        from .reportes import Reportes

        return Reportes
    if name == "RegresionLineal":
        from .regresion_lineal import RegresionLineal

        return RegresionLineal
    if name == "ClasificadorTexto":
        from .clasificador_text import ClasificadorTexto

        return ClasificadorTexto
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
