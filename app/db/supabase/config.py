from supabase import create_client, Client
from app.core.config import settings
from typing import Optional



SUPABASE_URL = settings.SUPABASE_URL
SUPABASE_KEY = settings.SUPABASE_API_KEY

supabase: Optional[Client] = None

if SUPABASE_URL !="" and SUPABASE_KEY != "":
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        print("✅ Supabase client created successfully.")
    except Exception as e:
        print(f"❌ Error creating Supabase client: {e}")
        supabase = None
else:
    print(F"[SUPABASE_URL]: {SUPABASE_URL} ", f"[SUPABASE_KEY]: {SUPABASE_KEY}")
    print("⚠️ SUPABASE_URL o SUPABASE_API_KEY no están configuradas. Cliente Supabase deshabilitado.")
    supabase = None

if __name__ == "__main__":
    print("Supabase client created successfully.")
    result = supabase.table("dolar").select("*").execute()
    print("Data from 'dolar' table:", result.data)