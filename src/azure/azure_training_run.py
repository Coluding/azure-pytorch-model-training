import os
try:
    from .azure_connection import AzureConnection
except ImportError:
    from azure_connection import AzureConnection


def main():
    #os.chdir("")
    azure_con = AzureConnection()
    #azure_con.run_script()


if __name__ == "__main__":
    main()