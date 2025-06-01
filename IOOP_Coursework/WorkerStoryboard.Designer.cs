namespace assignment
{
    partial class WorkerStoryboard
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
            this.btnUpdateStatus = new System.Windows.Forms.Button();
            this.lblJobStatus = new System.Windows.Forms.Label();
            this.lblRequests = new System.Windows.Forms.Label();
            this.btnRefreshRequests = new System.Windows.Forms.Button();
            this.lblWorkerMenu = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // btnUpdateStatus
            // 
            this.btnUpdateStatus.Location = new System.Drawing.Point(178, 280);
            this.btnUpdateStatus.Name = "btnUpdateStatus";
            this.btnUpdateStatus.Size = new System.Drawing.Size(191, 47);
            this.btnUpdateStatus.TabIndex = 0;
            this.btnUpdateStatus.Text = "Update Status";
            this.btnUpdateStatus.UseVisualStyleBackColor = true;
            // 
            // lblJobStatus
            // 
            this.lblJobStatus.AutoSize = true;
            this.lblJobStatus.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblJobStatus.Location = new System.Drawing.Point(224, 228);
            this.lblJobStatus.Name = "lblJobStatus";
            this.lblJobStatus.Size = new System.Drawing.Size(106, 25);
            this.lblJobStatus.TabIndex = 1;
            this.lblJobStatus.Text = "Job Status";
            this.lblJobStatus.Click += new System.EventHandler(this.label1_Click);
            // 
            // lblRequests
            // 
            this.lblRequests.AutoSize = true;
            this.lblRequests.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblRequests.Location = new System.Drawing.Point(596, 228);
            this.lblRequests.Name = "lblRequests";
            this.lblRequests.Size = new System.Drawing.Size(94, 25);
            this.lblRequests.TabIndex = 2;
            this.lblRequests.Text = "Requests";
            // 
            // btnRefreshRequests
            // 
            this.btnRefreshRequests.Location = new System.Drawing.Point(546, 280);
            this.btnRefreshRequests.Name = "btnRefreshRequests";
            this.btnRefreshRequests.Size = new System.Drawing.Size(191, 47);
            this.btnRefreshRequests.TabIndex = 3;
            this.btnRefreshRequests.Text = "Refresh Requests";
            this.btnRefreshRequests.UseVisualStyleBackColor = true;
            // 
            // lblWorkerMenu
            // 
            this.lblWorkerMenu.AutoSize = true;
            this.lblWorkerMenu.Font = new System.Drawing.Font("Microsoft Sans Serif", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblWorkerMenu.Location = new System.Drawing.Point(367, 132);
            this.lblWorkerMenu.Name = "lblWorkerMenu";
            this.lblWorkerMenu.Size = new System.Drawing.Size(193, 32);
            this.lblWorkerMenu.TabIndex = 4;
            this.lblWorkerMenu.Text = "Worker Menu";
            // 
            // WorkerStoryboard
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.ClientSize = new System.Drawing.Size(917, 523);
            this.Controls.Add(this.lblWorkerMenu);
            this.Controls.Add(this.btnRefreshRequests);
            this.Controls.Add(this.lblRequests);
            this.Controls.Add(this.lblJobStatus);
            this.Controls.Add(this.btnUpdateStatus);
            this.Name = "WorkerStoryboard";
            this.Text = "Worker Storyboard";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnUpdateStatus;
        private System.Windows.Forms.Label lblJobStatus;
        private System.Windows.Forms.Label lblRequests;
        private System.Windows.Forms.Button btnRefreshRequests;
        private System.Windows.Forms.Label lblWorkerMenu;
    }
}