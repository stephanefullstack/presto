#ifndef __prepsubband_cmd__
#define __prepsubband_cmd__
/*****
  command line parser interface -- generated by clig 
  (http://wsd.iitb.fhg.de/~geg/clighome/)

  The command line parser `clig':
  (C) 1995-2004 Harald Kirsch (clig@geggus.net)
*****/

typedef struct s_Cmdline {
  /***** -o: Root of the output file names */
  char outfileP;
  char* outfile;
  int outfileC;
  /***** -pkmb: Raw data in Parkes Multibeam format */
  char pkmbP;
  /***** -gmrt: Raw data in GMRT Phased Array format */
  char gmrtP;
  /***** -bcpm: Raw data in Berkeley-Caltech Pulsar Machine (BPP) format */
  char bcpmP;
  /***** -spigot: Raw data in Caltech-NRAO Spigot Card format */
  char spigotP;
  /***** -filterbank: Raw data in SIGPROC filterbank format */
  char filterbankP;
  /***** -psrfits: Raw data in PSRFITS format */
  char psrfitsP;
  /***** -noweights: Do not apply PSRFITS weights */
  char noweightsP;
  /***** -noscales: Do not apply PSRFITS scales */
  char noscalesP;
  /***** -nooffsets: Do not apply PSRFITS offsets */
  char nooffsetsP;
  /***** -wapp: Raw data in Wideband Arecibo Pulsar Processor (WAPP) format */
  char wappP;
  /***** -window: Window correlator lags with a Hamming window before FFTing */
  char windowP;
  /***** -numwapps: Number of WAPPs used with contiguous frequencies */
  char numwappsP;
  int numwapps;
  int numwappsC;
  /***** -if: A specific IF to use if available (summed IFs is the default) */
  char ifsP;
  int ifs;
  int ifsC;
  /***** -clip: Time-domain sigma to use for clipping (0.0 = no clipping, 6.0 = default */
  char clipP;
  float clip;
  int clipC;
  /***** -noclip: Do not clip the data.  (The default is to _always_ clip!) */
  char noclipP;
  /***** -invert: For rawdata, flip (or invert) the band */
  char invertP;
  /***** -zerodm: Subtract the mean of all channels from each sample (i.e. remove zero DM) */
  char zerodmP;
  /***** -runavg: Running mean subtraction from the input data */
  char runavgP;
  /***** -sub: Write subbands instead of de-dispersed data */
  char subP;
  /***** -subdm: The DM to use when de-dispersing subbands for -sub */
  char subdmP;
  double subdm;
  int subdmC;
  /***** -numout: Output this many values.  If there are not enough values in the original data file, will pad the output file with the average value */
  char numoutP;
  int numout;
  int numoutC;
  /***** -nobary: Do not barycenter the data */
  char nobaryP;
  /***** -DE405: Use the DE405 ephemeris for barycentering instead of DE200 (the default) */
  char de405P;
  /***** -lodm: The lowest dispersion measure to de-disperse (cm^-3 pc) */
  char lodmP;
  double lodm;
  int lodmC;
  /***** -dmstep: The stepsize in dispersion measure to use(cm^-3 pc) */
  char dmstepP;
  double dmstep;
  int dmstepC;
  /***** -numdms: The number of DMs to de-disperse */
  char numdmsP;
  int numdms;
  int numdmsC;
  /***** -nsub: The number of sub-bands to use */
  char nsubP;
  int nsub;
  int nsubC;
  /***** -downsamp: The number of neighboring bins to co-add */
  char downsampP;
  int downsamp;
  int downsampC;
  /***** -mask: File containing masking information to use */
  char maskfileP;
  char* maskfile;
  int maskfileC;
  /***** uninterpreted command line parameters */
  int argc;
  /*@null*/char **argv;
  /***** the whole command line concatenated */
  char *full_cmd_line;
} Cmdline;


extern char *Program;
extern void usage(void);
extern /*@shared*/Cmdline *parseCmdline(int argc, char **argv);

extern void showOptionValues(void);

#endif

