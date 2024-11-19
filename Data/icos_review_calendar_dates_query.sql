SET NOCOUNT ON;
DECLARE    @vd           INT          = NULL,
           @calendarType VARCHAR(200) = NULL,    
           @indexSymbol VARCHAR(20)   ='{}',	
           @calendarYearMonth INT     = {};
SET @vd = null

SELECT * FROM [sid].[tvfIndexCalendarDetailByYearMonth](@vd, @calendarYearMonth, @indexSymbol, @calendarType);