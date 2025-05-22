from db import engine
from models import OHLCVData, ExtendedHourData, Base

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created.")
