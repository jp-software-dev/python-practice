def calcular_propinas():
   
   try:
       total_cuenta = float(input("¿Cuál es el total de la cuenta? "))
       porcentaje_propina = int(input("¿Qué porcentaje de propina te gustaría dejar? "))
       numero_personas = int(input("¿Entre cuántas personas se va a dividir la cuenta?: "))

       propina_total = total_cuenta * (porcentaje_propina / 100)
       total_con_propina = total_cuenta + propina_total
       pago_por_persona = total_con_propina / numero_personas

       print("\n--- Cuenta ---")
       print(f"Monto de la propina: ${propina_total:.2f}")
       print(f"Total a pagar: ${total_con_propina:.2f}")
       print(f"Cada persona debe pagar: ${pago_por_persona:.2f}")

   except ValueError:
       print("\nError: Por favor, ingresa únicamente valores numéricos.")

if __name__ == "__main__":
    calcular_propinas()