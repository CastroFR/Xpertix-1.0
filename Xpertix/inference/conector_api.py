import os
from pathlib import Path
from pyswip import Prolog

def obtener_recomendacion(tarea):
    """Obtiene una recomendación de asignación de recursos basada en habilidades y disponibilidad."""
    try:
        prolog = Prolog()
        #ruta_archivo = Path("inference") / "motor.pl"
        ruta_archivo = Path(__file__).parent / "motor.pl"
        #ruta_archivo = Path(__file__).parent.parent / "inference" / "motor.pl"
        ruta_archivo_str = ruta_archivo.as_posix() # Forzar el uso de barras inclinadas

        #ruta_archivo_prolog = ruta_archivo.as_posix()
        
        print(f"Consultando archivo Prolog en: {ruta_archivo.resolve()}")
        #ruta_archivo = str(ruta_archivo).replace("\\", "/")
        
        prolog.consult(ruta_archivo_str)

        resultado = list(prolog.query(f"recomendacion_asignacion('{tarea}', Recurso)", maxresult=1))
        print("Resultado de Prolog:", resultado)

        if resultado:
            return [r['Recurso'] for r in resultado]
        else:
            return ["No hay recursos disponibles adecuados para la asignación"]
    except Exception as e:
        print(f"Error en la consulta a Prolog: {e}")
        return None

def optimizar_carga_trabajo(tarea):
    """Consulta Prolog para obtener una recomendación de optimización de carga de trabajo."""
    prolog = Prolog()
    prolog.consult("inference/motor.pl")
    resultado = list(prolog.query(f"optimizar_carga(Recurso, '{tarea}')"))
    return [r['Recurso'] for r in resultado] if resultado else ["No se encontraron recursos para optimizar la carga de trabajo"]

def ajustar_asignacion(tarea, recurso_anterior, recurso_nuevo):
    """Ajusta la asignación de recursos en función de la disponibilidad."""
    prolog = Prolog()
    prolog.consult("inference/motor.pl")
    resultado = list(prolog.query(f"ajuste_asignacion('{tarea}', '{recurso_anterior}', '{recurso_nuevo}')"))
    return len(resultado) > 0

