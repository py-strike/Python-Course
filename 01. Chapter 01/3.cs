string printer_name = mySettingsGlobal[0].printer_a4;

System.Windows.Controls.PrintDialog printDialog = new System.Windows.Controls.PrintDialog();

// ADDED: Direct printer setup using LocalPrintServer
PrintQueue printQueue = null;
if (!string.IsNullOrEmpty(printer_name))
{
    try
    {
        PrintServer printServer = new LocalPrintServer();
        printQueue = printServer.GetPrintQueue(printer_name);
    }
    catch (Exception ex)
    {
        MessageBox.Show($"Failed to set up the printer: {ex.Message}", "Error", MessageBoxButton.OK, MessageBoxImage.Error);
        return;
    }
}
else
{
    MessageBox.Show("veuillez configurer l'imprimante svp.", "Erreur", MessageBoxButton.OK, MessageBoxImage.Error);
    return;
}

// ADDED: Check if the printQueue is valid
if (printQueue == null)
{
    MessageBox.Show("The specified printer is not installed. Please check your printer settings.", "Printer Not Found", MessageBoxButton.OK, MessageBoxImage.Error);
    return;
}



try{
    
}