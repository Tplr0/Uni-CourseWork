namespace assignment
{
    partial class RequestsFromCustomer
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.lblStatus = new System.Windows.Forms.Label();
            this.cmbRequestsStatus = new System.Windows.Forms.ComboBox();
            this.dgvRequests = new System.Windows.Forms.DataGridView();
            this.btnRefresh = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.dgvRequests)).BeginInit();
            this.SuspendLayout();
            // 
            // lblStatus
            // 
            this.lblStatus.AutoSize = true;
            this.lblStatus.Font = new System.Drawing.Font("Microsoft Sans Serif", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblStatus.Location = new System.Drawing.Point(362, 134);
            this.lblStatus.Name = "lblStatus";
            this.lblStatus.Size = new System.Drawing.Size(237, 32);
            this.lblStatus.TabIndex = 0;
            this.lblStatus.Text = "Requests Status";
            // 
            // cmbRequestsStatus
            // 
            this.cmbRequestsStatus.FormattingEnabled = true;
            this.cmbRequestsStatus.Location = new System.Drawing.Point(207, 201);
            this.cmbRequestsStatus.Name = "cmbRequestsStatus";
            this.cmbRequestsStatus.Size = new System.Drawing.Size(282, 24);
            this.cmbRequestsStatus.TabIndex = 2;
            // 
            // dgvRequests
            // 
            this.dgvRequests.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvRequests.Location = new System.Drawing.Point(188, 249);
            this.dgvRequests.Name = "dgvRequests";
            this.dgvRequests.RowHeadersWidth = 51;
            this.dgvRequests.RowTemplate.Height = 24;
            this.dgvRequests.Size = new System.Drawing.Size(573, 217);
            this.dgvRequests.TabIndex = 3;
            // 
            // btnRefresh
            // 
            this.btnRefresh.Location = new System.Drawing.Point(573, 195);
            this.btnRefresh.Name = "btnRefresh";
            this.btnRefresh.Size = new System.Drawing.Size(169, 35);
            this.btnRefresh.TabIndex = 4;
            this.btnRefresh.Text = "Refresh Requests";
            this.btnRefresh.UseVisualStyleBackColor = true;
            // 
            // RequestsFromCustomer
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.ClientSize = new System.Drawing.Size(946, 561);
            this.Controls.Add(this.btnRefresh);
            this.Controls.Add(this.dgvRequests);
            this.Controls.Add(this.cmbRequestsStatus);
            this.Controls.Add(this.lblStatus);
            this.Name = "RequestsFromCustomer";
            this.Text = "Requests From Customer";
            ((System.ComponentModel.ISupportInitialize)(this.dgvRequests)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lblStatus;
        private System.Windows.Forms.ComboBox cmbRequestsStatus;
        private System.Windows.Forms.DataGridView dgvRequests;
        private System.Windows.Forms.Button btnRefresh;
    }
}