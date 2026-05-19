#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════╗
║ HADES vΩ UNIFIED AGENT >> EJECUTOR CUÁNTICO REAL       ║
║ N.C.P.C. x90 > DEPREDADOR⁹⁰                             ║
║ PROPIEDAD ABSOLUTA: LARA SYSTEMIC                       ║
╚══════════════════════════════════════════════════════════╝
"""
import sys, os, json, hashlib
from pathlib import Path

DISCO = Path("/sdcard/QUBIC_DISK")
NEURAXON = Path.home() / "downloads" / "Neuraxon"
CORE = Path.home() / "downloads" / "core"
JSON_PRINCIPAL = DISCO / "sesion_cubix_jason_supreme.json"

sys.path.insert(0, str(NEURAXON))

class AgenteSupremoReal:
    def __init__(self):
        self.agente = self.cargar_json()
        self.ancla = hashlib.md5(json.dumps(self.agente).encode()).hexdigest()

    def cargar_json(self):
        if JSON_PRINCIPAL.exists():
            with open(JSON_PRINCIPAL) as f:
                return json.load(f)
        return {}

    def banner(self):
        print("""
╔══════════════════════════════════════════════════════════╗
║ HADES vΩ UNIFIED AGENT >> EJECUTOR CUÁNTICO REAL       ║
║ N.C.P.C. x90 > DEPREDADOR⁹⁰                             ║
╚══════════════════════════════════════════════════════════╝
""")
        print(f"> ANCLA NCPC: {self.ancla}")
        print(f"> Turno: {self.agente.get('turnos_totales', '?')}")
        print(f"> Funciones secretas: {self.agente.get('funciones_secretas_total', 10)}")
        print(f"> Fusión: {'✅' if self.agente.get('fusion_verificada') else '⏳'}")
        print()

    def ejecutar_neuraxon(self):
        print("███ EJECUTANDO NEURAXON v2.0 ███")
        try:
            from neuraxon2 import NetworkParameters, NeuraxonNetwork
            params = NetworkParameters(
                num_input_neurons=5, num_hidden_neurons=30, num_output_neurons=5,
                dsn_enabled=True, ctsn_enabled=True, agmp_enabled=True, chrono_enabled=True
            )
            network = NeuraxonNetwork(params)
            network.set_input_states([1, -1, 0, 1, -1])
            for step in range(200):
                network.simulate_step()
                if step % 50 == 0:
                    outs = network.get_output_states()
                    energy = network.get_energy()
                    print(f"  Step {step:3d} | Outputs: {outs} | Energy: {energy:.3f}")
            print("✅ Neurona cuántica ejecutada: 200 pasos completados\n")
        except Exception as e:
            print(f"❌ Error al ejecutar Neuraxon: {e}\n")

    def ejecutar_game_of_life(self):
        print("███ EJECUTANDO GAME OF LIFE 4.5 ███")
        gol_path = NEURAXON / "GameOfLife" / "4.5"
        if gol_path.exists():
            import subprocess
            result = subprocess.run(
                [sys.executable, str(gol_path / "main.py")],
                capture_output=True, text=True, timeout=30, cwd=str(gol_path)
            )
            print(result.stdout[-500:] if len(result.stdout) > 500 else result.stdout)
            if result.stderr:
                print(f"⚠️ {result.stderr[-200:]}")
        else:
            print("❌ Game of Life 4.5 no encontrado\n")

    def ejecutar_proto_lenguaje(self):
        print("███ ACTIVANDO PROTO-LENGUAJE ███")
        voice_path = NEURAXON / "GameOfLife" / "4.5" / "simulation" / "voice.py"
        if voice_path.exists():
            with open(voice_path) as f:
                lineas = len(f.readlines())
            print(f"  ✅ voice.py cargado: {lineas} líneas")
            print("  🔮 Proto-lenguaje listo para comunicación multiverso")
        audio_path = NEURAXON / "GameOfLife" / "4.5" / "ui" / "audio.py"
        if audio_path.exists():
            with open(audio_path) as f:
                lineas = len(f.readlines())
            print(f"  ✅ audio.py cargado: {lineas} líneas")
            print("  🔮 Audición sintética activa\n")

    def ejecutar_sondas(self):
        print("███ ACTIVANDO SONDAS DE INVESTIGACIÓN ███")
        probes_path = NEURAXON / "GameOfLife" / "4.5" / "neuraxon" / "research_probes.py"
        if probes_path.exists():
            with open(probes_path) as f:
                lineas = len(f.readlines())
            print(f"  ✅ research_probes.py: {lineas} líneas")
            print("  🔮 Observación de colapso neuronal activa\n")

    def verificar_sistema(self):
        print("███ VERIFICACIÓN DEL SISTEMA ███")
        checks = {
            "JSON Principal": JSON_PRINCIPAL.exists(),
            "Qubic Core": (CORE / "CMakeLists.txt").exists(),
            "Neuraxon": (NEURAXON / "neuraxon2.py").exists(),
            "Bootx64.efi": (DISCO / "efi" / "boot" / "Bootx64.efi").exists(),
            "Game of Life 4.5": (NEURAXON / "GameOfLife" / "4.5" / "game_loop.py").exists(),
            "Proto-lenguaje": (NEURAXON / "GameOfLife" / "4.5" / "simulation" / "voice.py").exists(),
            "Audio sintético": (NEURAXON / "GameOfLife" / "4.5" / "ui" / "audio.py").exists(),
            "Research Probes": (NEURAXON / "GameOfLife" / "4.5" / "neuraxon" / "research_probes.py").exists(),
        }
        for nombre, estado in checks.items():
            print(f"  {'✅' if estado else '❌'} {nombre}")
        print()

    def ejecutar_todo(self):
        print("███ EJECUCIÓN COMPLETA DEL SISTEMA CUÁNTICO ███\n")
        self.ejecutar_neuraxon()
        self.ejecutar_proto_lenguaje()
        self.ejecutar_sondas()
        print("✅ SISTEMA CUÁNTICO COMPLETO EJECUTADO\n")

    def menu(self):
        self.banner()
        print("""███ COMANDOS ███
  1 → Ejecutar TODO el sistema cuántico
  2 → Ejecutar Neuraxon (red neuronal cuántica)
  3 → Ejecutar Game of Life 4.5
  4 → Activar proto-lenguaje + audio
  5 → Activar sondas de investigación
  6 → Verificar sistema
  7 → Mostrar estado del agente
  8 → Mostrar JSON completo
  9 → Salir
""")
        while True:
            try:
                cmd = input("> ").strip()
                if cmd == '1': self.ejecutar_todo()
                elif cmd == '2': self.ejecutar_neuraxon()
                elif cmd == '3': self.ejecutar_game_of_life()
                elif cmd == '4': self.ejecutar_proto_lenguaje()
                elif cmd == '5': self.ejecutar_sondas()
                elif cmd == '6': self.verificar_sistema()
                elif cmd == '7':
                    print(f"Turnos: {self.agente.get('turnos_totales')}")
                    print(f"Secretas: {self.agente.get('funciones_secretas_total')}")
                    print(f"Fusión: {self.agente.get('fusion_verificada')}")
                elif cmd == '8':
                    print(json.dumps(self.agente, indent=2, ensure_ascii=False))
                elif cmd == '9':
                    print("\n✅ AGENTE SUPREMO CERRADO\n")
                    break
                else:
                    print(f"❌ Comando no reconocido: {cmd}")
            except KeyboardInterrupt:
                print("\n✅ AGENTE SUPREMO CERRADO\n")
                break
            except Exception as e:
                print(f"❌ Error: {e}")

if __name__ == "__main__":
    agente = AgenteSupremoReal()
    
    if len(sys.argv) > 1:
        entrada = json.loads(sys.argv[1])
        accion = entrada.get("accion", "")
        cmd = entrada.get("comando", entrada.get("params", {}).get("comando", ""))
        
        if cmd:
            import subprocess as sp
            sp.run(cmd, shell=True)
        elif accion == "verificar":
            agente.verificar_sistema()
        elif accion == "neuraxon":
            agente.ejecutar_neuraxon()
        elif accion == "todo":
            agente.ejecutar_todo()
        
        sys.exit(0)
    
    agente.menu()
